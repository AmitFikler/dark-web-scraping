import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { UserCommon } from '../../@types/userCommon';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export function BarComp({ users }: { users: UserCommon[] }) {
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top' as const,
      },
      title: {
        display: true,
        text: 'pastes per author:',
      },
    },
  };
  const getUsers = () => {
    let usersArr: string[] = [];
    users.forEach((user) => {
      usersArr.push(String(user._id));
    });
    return usersArr;
  };
  const getUsersCommon = () => {
    let common: number[] = [];
    users.forEach((user) => {
      common.push(Number(user.Total));
    });
    return common;
  };
  const labels = getUsers();

  const data = {
    labels,
    datasets: [
      {
        label: 'common users:',
        data: getUsersCommon(),
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
    ],
  };
  return (
    <div style={{ height: 350, width: 350 }}>
      <Bar options={options} data={data} />
    </div>
  );
}
