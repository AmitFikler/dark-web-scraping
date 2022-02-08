import { useEffect, useState } from 'react';
import axios from 'axios';
import { Paste } from '../@types/paste';
import Pastes from './components/pastes';

function App() {
  const [pastes, setPastes] = useState<Paste[]>([]);

  useEffect(() => {
    fetchPaste();
    setInterval(fetchPaste, 120000);
  }, []);

  const fetchPaste = async () => {
    const { data } = await axios.get('http://127.0.0.1:8000/data');
    console.log('FETCHED');
    setPastes((prevPastes) => [...prevPastes, ...data]);
  };
  return (
    <div className="App">
      <h1>hello world</h1>
      {pastes?.map((paste) => (
        <Pastes paste={paste} />
      ))}
    </div>
  );
}

export default App;
