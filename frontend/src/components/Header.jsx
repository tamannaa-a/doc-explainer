import React from "react";
export default function Header(){
  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-6 py-4 flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-lg bg-gradient-to-r from-brand-500 to-brand-700 flex items-center justify-center text-white font-bold">DE</div>
          <div>
            <h1 className="text-lg font-semibold">Doc Explainer</h1>
            <p className="text-sm text-gray-500">Document Classification • Claims Explanation</p>
          </div>
        </div>
        <nav className="space-x-4">
          <a className="text-sm text-gray-600 hover:text-brand-700" href="#">Docs</a>
          <a className="text-sm text-gray-600 hover:text-brand-700" href="#">Contact</a>
        </nav>
      </div>
    </header>
  );
}
