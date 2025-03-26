import React from "react";
import { useState } from "react";

function Header() {
  const [whatIsStruct, setWhatIsStruct] = useState(true);
  return (
    <div>
      <div className="grid grid-cols-1 gap-4">
        <div className=" rounded bg-[#111827] p-2 border border-[#111827]">
          <div>
            <label htmlFor="Notes">
              <span className="text-lg font-medium text-[#5EEAD4]">
                {" "}
                Input Transaction Details{" "}
              </span>

              <div className="relative mt-0.5 overflow-hidden rounded focus-within:ring focus-within:ring-blue-600 dark:border-gray-600">
                {whatIsStruct ? (
                  <textarea
                    id="Notes"
                    className="w-full p-2 rounded resize-none border-none focus:ring-0 "
                    rows="15"
                  ></textarea>
                ) : (
                  <></>
                )}

                <div className="flex items-center justify-end gap-2 p-1.5">
                  <button
                    type="button"
                    className="rounded border border-transparent px-3 py-1.5 text-sm font-medium text-gray-700 transition-colors hover:border-black hover:text-gray-900 dark:text-gray-200 dark:hover:text-white"
                    onClick={() => setWhatIsStruct(!whatIsStruct)}
                  >
                    Switch to JSON Format
                  </button>
                  <button
                    type="button"
                    className="rounded border border-transparent px-3 py-1.5 text-sm font-medium text-gray-700 transition-colors hover:border-black hover:text-gray-900 dark:text-gray-200 dark:hover:text-white"
                  >
                    Clear
                  </button>

                  <button
                    type="button"
                    className="rounded border border-gray-300 px-3 py-1.5 text-sm font-medium text-gray-900 shadow-sm transition-colors hover:bg-gray-100 dark:border-gray-600 dark:text-white dark:hover:bg-gray-700"
                  >
                    Calculate Risk Assessment
                  </button>
                </div>
              </div>
            </label>
          </div>
        </div>
        <div className="h-32 rounded bg-gray-300">
          <div className="h-32 rounded bg-gray-300"></div>
          <div className="h-32 rounded bg-gray-300"></div>
        </div>
      </div>
    </div>
  );
}

export default Header;
