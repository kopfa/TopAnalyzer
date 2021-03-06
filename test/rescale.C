void rescale()
{
  //const double wDYmm[] = {1.0,1.0,1.0,1.02,0.96,1.07,1.20};
  //const double wDYee[] = {1.0,1.0,1.0,1.03,1.00,1.22,1.33};
  const double wDYmm[] = {1.0,1.0,1.0,1.0,1.0,1.0,1.0};
  const double wDYee[] = {1.0,1.0,1.0,1.0,1.0,1.0,1.0};

  const int nDYmm = sizeof(wDYmm)/sizeof(wDYmm[0]);
  const int nDYee = sizeof(wDYee)/sizeof(wDYee[0]);

  rescale("/data/export/common/Top/finalHisto/v5/MuMu.root", "MuMu_DYll_up.root", "hMC_DYll_", wDYmm, nDYmm, +0.5, 1.3);
  rescale("/data/export/common/Top/finalHisto/v5/MuMu.root", "MuMu_DYll_dw.root", "hMC_DYll_", wDYmm, nDYmm, -0.5, 0.7);

  rescale("/data/export/common/Top/finalHisto/v5/MuEl.root", "MuEl_DYll_up.root", "hMC_DYll_", wDYmm, nDYmm, +0.5, 1.3);
  rescale("/data/export/common/Top/finalHisto/v5/MuEl.root", "MuEl_DYll_dw.root", "hMC_DYll_", wDYmm, nDYmm, -0.5, 0.7);

  rescale("/data/export/common/Top/finalHisto/v5/ElEl.root", "ElEl_DYll_up.root", "hMC_DYll_", wDYee, nDYee, +0.5, 1.3);
  rescale("/data/export/common/Top/finalHisto/v5/ElEl.root", "ElEl_DYll_dw.root", "hMC_DYll_", wDYee, nDYee, -0.5, 0.7);

}

void rescale(TString inFileName, TString outFileName, TString histNamePrefix,
             const double* wDYll, const int nDYll, const double variation = 0, const double scaleAllMC = 1.0)
{
  TFile* inFile = TFile::Open(inFileName);
  TFile* outFile = TFile::Open(outFileName, "RECREATE");
  
  TList* inDirs = inFile->GetListOfKeys();
  for ( int i=0; i<nDYll; ++i )
  {
    TDirectory* inDir = dynamic_cast<TDirectory*>(inFile->Get(Form("Step_%d", i+1)));
    if ( !inDir ) continue;

    TDirectory* outDir = outFile->mkdir(Form("Step_%d", i+1));

    TList* inHists = inDir->GetListOfKeys();
    for ( int j=0; j<inHists->GetSize(); ++j )
    {
      TString histName = inHists->At(j)->GetName();

      TH1F* hSrc = dynamic_cast<TH1F*>(inDir->Get(histName));
      if ( !hSrc ) continue;

      outDir->cd();
      TH1F* h = (TH1F*)hSrc->Clone();

      if ( histName.Contains("gen") ) continue;

      if ( histName.BeginsWith(histNamePrefix) )
      {
        h->Scale(wDYll[i]*(1.+variation));
      }
      else if ( histName.BeginsWith("hMC_") )
      {
        h->Scale(scaleAllMC);
      }
    }
  }

  outFile->Write();
  outFile->Close();

  inFile->Close();
}

