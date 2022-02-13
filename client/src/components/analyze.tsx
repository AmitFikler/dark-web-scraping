import axios from 'axios';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Common } from '../../@types/common';
import { UserCommon } from '../../@types/userCommon';
import PieComp from './pie';

function Analyze() {
  const [commonWords, setCommonWords] = useState<Common>();
  const [commonTitles, setCommonTitles] = useState<Common>();
  const [TotalPastes, setTotalPastes] = useState<Number>();
  const [PastesPerAuthor, setPastesPerAuthor] = useState<UserCommon[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    console.log('use effect');
    getContentCommonWord().then((res) => setCommonWords(res));
    getTitleCommonWord().then((res) => setCommonTitles(res));
    getTotalPastes().then((res) => setTotalPastes(res));
    getPastesPerAuthor().then((res) => setPastesPerAuthor(res));
    setInterval(() => {
      getContentCommonWord().then((res) => setCommonWords(res));
      getTitleCommonWord().then((res) => setCommonTitles(res));
      getTotalPastes().then((res) => setTotalPastes(res));
      getPastesPerAuthor().then((res) => setPastesPerAuthor(res));
    }, 120000);
  }, []);
  const getContentCommonWord = async () => {
    const { data } = await axios.get(
      'http://127.0.0.1:8000/analysis/common_Words_content'
    );
    return data;
  };

  const getTitleCommonWord = async () => {
    const { data } = await axios.get(
      'http://127.0.0.1:8000/analysis/common_Words_title'
    );
    return data;
  };

  const getTotalPastes = async () => {
    const { data } = await axios.get(
      'http://127.0.0.1:8000/analysis/total_amount'
    );
    return data;
  };

  const getPastesPerAuthor = async () => {
    const { data } = await axios.get(
      'http://127.0.0.1:8000/analysis/per_author'
    );
    return data;
  };

  const getUsers = () => {
    let usersArr: string[] = [];
    PastesPerAuthor.forEach((user) => {
      usersArr.push(String(user._id));
    });
    return usersArr;
  };
  const getUsersCommon = () => {
    let common: number[] = [];
    PastesPerAuthor.forEach((user) => {
      common.push(Number(user.Total));
    });
    return common;
  };
  return (
    <>
      <h1>Analyze</h1>
      <div className="navigateBtn" onClick={() => navigate('/')}>
        <button>Home</button>
      </div>
      <div className="analyzes">
        {commonWords ? (
          <PieComp
            labels={Object.keys(commonWords).map(
              (common) => common.split('_')[2]
            )}
            data={Object.values(commonWords)}
            title="Common Words:"
          />
        ) : (
          <p>loading...</p>
        )}
        {commonTitles ? (
          <PieComp
            labels={Object.keys(commonTitles).map(
              (common) => common.split('_')[2]
            )}
            data={Object.values(commonTitles)}
            title="Common Titles:"
          />
        ) : (
          <p>loading...</p>
        )}
        {PastesPerAuthor ? (
          <PieComp
            labels={getUsers()}
            data={getUsersCommon()}
            title="Pastes per author:"
          />
        ) : (
          <p>loading...</p>
        )}
      </div>
      <h3>Total Pastes: {TotalPastes}</h3>
    </>
  );
}

export default Analyze;
