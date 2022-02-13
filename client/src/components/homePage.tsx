import axios from 'axios';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Paste } from '../../@types/paste';
import Pastes from './pastes';

function HomePage() {
  const [pastes, setPastes] = useState<Paste[]>([]);
  const [input, setInput] = useState<string>('');
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetchPaste();
    setInterval(fetchPaste, 6000000);
  }, []);

  const fetchPaste = async () => {
    const { data } = await axios.get('http://127.0.0.1:8000/data');
    console.log('FETCHED');
    setPastes((prevPastes) => [...prevPastes, ...data]);
    setIsLoading(false);
  };

  const onChangeInput = () => {};

  return (
    <>
      <h1>DARK WEB SCRAPING</h1>
      <div className="navigateBtn" onClick={() => navigate('/analyze')}>
        <button>Analyzer</button>
      </div>
      <input type={'text'}></input>
      {isLoading ? (
        <div>
          <span className="loader"></span>
        </div>
      ) : (
        <div className="pastes">
          {pastes ? (
            pastes.map((paste) => <Pastes paste={paste} />)
          ) : (
            <p>Loading...</p>
          )}
        </div>
      )}
    </>
  );
}

export default HomePage;
