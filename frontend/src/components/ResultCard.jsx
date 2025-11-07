import React from "react";

export default function ResultCard({ result }) {
  if(!result) return null;
  return (
    <div className="mt-6 bg-white rounded-lg shadow p-6">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-xl font-semibold">{result.document_type}</h3>
          <p className="text-sm text-gray-500">Confidence: {(result.confidence*100).toFixed(1)}%</p>
        </div>
      </div>

      <div className="mt-4">
        <h4 className="text-sm font-medium text-gray-700">Explanation</h4>
        <p className="mt-2 text-gray-700">{result.explanation}</p>
      </div>

      <div className="mt-4">
        <details className="text-sm">
          <summary className="font-medium">Preview extracted text</summary>
          <pre className="mt-2 text-xs text-gray-600 max-h-56 overflow-auto bg-gray-50 p-3 rounded">{result.preview}</pre>
        </details>
      </div>
    </div>
  );
}
