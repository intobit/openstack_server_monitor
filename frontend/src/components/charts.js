import { LineChart } from '@mui/x-charts/LineChart';
import { useState, useEffect } from "react";

function Charts({ activeStatus }) {
    const [xData, setXData] = useState([]);
    const [yData, setYData] = useState([]);

    useEffect(() => {
        const updateChartData = () => {
            const date = new Date();
            const currentTime = new Intl.DateTimeFormat('de-DE', {
                hour: "numeric",
                minute: "numeric",
            }).format(date);

            setXData(prevXData => [...prevXData, currentTime]);
            setYData(prevYData => [...prevYData, activeStatus ? 1 : 0]);
        };

        const intervalId = setInterval(updateChartData, 5000);

        return () => clearInterval(intervalId);
    }, [activeStatus]);

    return (
        <LineChart
            width={500}
            height={150}
            series={[{ data: yData, label:'uptime', area: true, showMark: false, color: 'rgba(37,180,69,0.81)'}]}
            xAxis={[{ scaleType: 'point', data: xData }]}
            sx={{
                '.MuiLineElement-root': {
                    display: 'none',
                },
            }}
            slotProps={{
                legend: {
                    direction: 'row',
                    position: {vertical: 'bottom', horizontal: 'middle'},
                    padding: 0,
                }
            }}
            margin={{
                left: 5,
                right: 5,
                top: 30,
                bottom: 50,
            }}
        />
    );
}

export default Charts;
