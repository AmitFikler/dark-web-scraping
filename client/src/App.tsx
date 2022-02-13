import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Analyze from './components/analyze';
import HomePage from './components/homePage';

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/analyze" element={<Analyze />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
