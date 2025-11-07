import React, { useState } from "react";
import Header from "./components/Header";
import UploadDropzone from "./components/UploadDropzone";
import ResultCard from "./components/ResultCard";
import { analyzeFile } from "./api";

export default function App(){
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState(null);

  async function handleFile(f){
    setFile(f);
    setResult(null);
    setError(null);
    setUploading(true);
    try{
      const res = await analyzeFile(f);
      setResult(res);
    }catch(e){
      console.error(e);
      setError(e?.response?.data?.error || e.message || "Server error");
    }finally{
      setUploading(false);
    }
  }

  return (
    <div>
      <Header />
      <main className="container mx-auto p-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="md:col-span-2">
            <UploadDropzone onFile={handleFile} uploading={uploading} />
            {error && (
              <div className="mt-4 p-4 bg-red-50 border border-red-200 text-red-700 rounded">{error}</div>
            )}
            <ResultCard result={result} />
          </div>

          <aside className="hidden md:block">
            <div className="bg-white rounded-lg p-6 shadow">
              <h3 className="font-semibold">How it works</h3>
              <ol className="mt-3 text-sm text-gray-600 space-y-2">
                <li>1. Upload a PDF</li>
                <li>2. Backend extracts text (OCR fallback)</li>
                <li>3. Model classifies and generates explanation</li>
                <li>4. Frontend shows type, confidence & explanation</li>
              </ol>
            </div>
          </aside>
        </div>
      </main>
    </div>
  )
}
