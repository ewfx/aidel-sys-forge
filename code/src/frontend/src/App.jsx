import Header from "./components/Header.jsx";
import QueryForm from "./components/QueryForm.jsx";

export default function App() {
  return (
    <div className="bg-[#5EEAD4]">
      <Header />
      <div className="p-2">
        <QueryForm />
      </div>
    </div>
  );
}
