import React, { useState, useEffect } from 'react';
import Chart from 'chart.js/auto';
import '../../Styles/graph.css'

function Graph() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/graph_data')
            .then(res => res.json())
            .then(data => {
                setData(data);
            })
            .catch(err => {
                console.log(err.message);
            });
    }, []);

    useEffect(() => {
        if (data.columns && data.values) {
            const ctx = document.getElementById('lineChart');
            const sum = data.values[0].reduce((acc, curr) => acc + curr, 0); 
            new Chart(ctx, {
                type: 'bar',
                data: { 
                    labels: data.columns,
                    datasets: [{
                        label: `No. of people (Line)`, 
                        data: data.values[0],
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderWidth: 2,
                        pointRadius: 5,
                        pointBackgroundColor: 'rgba(75, 192, 192, 1)',
                        tension: 0.4,
                        type: 'line',  
                        // type: 'bar',
                        yAxisID: 'y-axis-line' 
                    },{
                        label: `No. of people (Line)`, 
                        data: data.values[0],
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 2,
                        pointRadius: 5,
                        pointBackgroundColor: 'rgba(75, 192, 192, 1)',
                        tension: 0.4,
                        type: 'line',  
                        type: 'bar',
                        yAxisID: 'y-axis-line' 
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            id: 'y-axis-line',
                            type: 'linear',
                            position: 'left',
                            ticks: {
                                font: {
                                    size: 20,
                                    family: 'Arial',
                                },
                                color: 'black'
                            }
                        }, {
                            id: 'y-axis-bar',
                            type: 'linear',
                            position: 'right',
                            ticks: {
                                font: {
                                    size: 13,
                                    family: 'Arial',
                                },
                                color: 'black'
                            }
                        }],
                        x: {
                            ticks: {
                                font: {
                                    size: 13,
                                    family: 'Arial',
                                },
                                color: 'black'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'People we helped in the past 7 days',
                            font: {
                                size: 17
                            },
                            color: 'black'
                        },
                        legend: {
                            labels: {
                                font: {
                                    size: 15
                                }
                            }
                        }
                    }
                }
            });
        }
    }, [data]);

    return (
        <div className="overflow-auto max-h-80 max-w-xl p-3  bg-white border border-gray-500 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-900 dark:border-gray-900">
            <canvas id="lineChart"></canvas>
        </div>
    );
}

export default Graph;
