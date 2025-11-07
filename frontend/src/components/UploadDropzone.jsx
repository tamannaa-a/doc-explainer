import React, { useRef } from "react";
import classNames from "classnames";

export default function UploadDropzone({ onFile, uploading }) {
  const fileRef = useRef();

  function handleFile(e){
    const f = e.target.files[0];
    if(f) onFile(f);
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-sm">
      <div className="border-2 border-dashed border-gray-200 rounded-lg p-6 text-center">
        <div className="mb-4">
          <svg className="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M7 16V4m0 0h10M7 4l10 12M7 16h10" />
          </svg>
        </div>
        <h3 className="text-lg font-semibold">Drag & drop files here</h3>
        <p className="text-sm text-gray-500 mt-2">PDFs only. Max recommended size: 10MB</p>

        <div className="mt-6">
          <input ref={fileRef} type="file" accept="application/pdf" onChange={handleFile} className="hidden" />
          <button
            className={classNames(
              "px-4 py-2 rounded-md text-white font-medium",
              uploading ? "bg-gray-400 cursor-not-allowed" : "bg-brand-500 hover:bg-brand-700"
            )}
            onClick={() => fileRef.current.click()}
            disabled={uploading}
          >
            {uploading ? "Analyzing..." : "Select a PDF"}
          </button>
        </div>
      </div>
    </div>
  );
}
