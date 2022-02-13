import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

function PieComp({
  labels,
  data,
  title,
}: {
  labels: string[];
  data: number[];
  title: string;
}) {
  const dataForPie = {
    labels: labels,
    datasets: [
      {
        label: '# of Votes',
        data,
        backgroundColor: [
          'rgba(255, 99, 132,0.9)',
          'rgba(54, 162, 235,0.9)',
          'rgba(255, 206, 86,0.9)',
          'rgba(75, 192, 192,0.9)',
          'rgba(153, 102, 255,0.9)',
          'rgba(255, 159, 64,0.9)',
          'rgba(255, 255, 64,0.9)',
          'rgba(134, 159, 64,0.9)',
          'rgba(44, 159, 64,0.9)',
          'rgba(255, 159, 240,0.9)',
        ],
        borderColor: ['black'],
        borderWidth: 1,
      },
    ],
  };
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top' as const,
      },
      title: {
        display: true,
        text: title,
      },
    },
  };
  return (
    <div style={{ height: 350, width: 350 }}>
      <Pie data={dataForPie} options={options} />
    </div>
  );
}

export default PieComp;
