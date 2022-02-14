import axios from 'axios';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Paste } from '../../@types/paste';
import Pastes from './pastes';
import { DebounceInput } from 'react-debounce-input';

function HomePage() {
  const [pastes, setPastes] = useState<Paste[]>([]);
  const [input, setInput] = useState<string>('');
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetchPaste();
    setInterval(fetchPaste, 120000);
  }, []);

  const fetchPaste = async () => {
    const { data } = await axios.get('http://127.0.0.1:8000/data');
    console.log('FETCHED');
    setPastes((prevPastes) => [...prevPastes, ...data]);
    setIsLoading(false);
  };

  return (
    <>
      <h1>DARK WEB SCRAPING</h1>
      <div className="navigateBtn" onClick={() => navigate('/analyze')}>
        <button>Analyzer</button>
      </div>
      <DebounceInput
        minLength={2}
        debounceTimeout={500}
        onChange={(e) => setInput(e.target.value)}
      />
      {isLoading ? (
        <div>
          <span className="loader"></span>
        </div>
      ) : (
        <div className="pastes">
          {pastes ? (
            pastes
              .filter((paste) =>
                paste.Title.toLowerCase().includes(input.toLowerCase())
              )
              .map((paste) => <Pastes paste={paste} />)
          ) : (
            <p>Loading...</p>
          )}
        </div>
      )}
    </>
  );
}

export default HomePage;
