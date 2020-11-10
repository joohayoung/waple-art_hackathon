// var options = {
//     chart: {type: "area", height: 300, foreColor: "#ffffff", stacked: true,
//     dropShadow: {enabled: true, enabledSeries: [0], top: -2, left: 2, blur: 5,opacity: 0.06}},
//     colors: ['#ff540a'], //차트 색상 
//     stroke: {curve: "smooth",width: 3},
//     dataLabels: {enabled: false},
//     series: [
//     {name: 'first data', data: generateDayWiseTimeSeries(7, 1)},
//     // {name: 'second data', data: generateDayWiseTimeSeries(1, 18)}
//     ],
//     markers: {size: 0, strokeColor: "#fff", strokeWidth: 3,
//     strokeOpacity: 1, fillOpacity: 1,hover: {size: 6}},
//     xaxis: {type: "datetime", axisBorder: {show: false}, axisTicks: {show: false}},
//     yaxis: {labels: {offsetX: 14,offsetY: -5},tooltip: {enabled: true}},
//     grid: {padding: {left: -5,right: 5}},
//     tooltip: {x: {format: "dd MMM yyyy"},},
//     legend: {position: 'top', horizontalAlign: 'left'},
//     fill: { type: "solid", fillOpacity: 0.5}
//     };

var options = {
    series: [{
        name: '남성',
        data: weekvalue(0) //[44, 55, 57, 56, 61, 58, 63] //
        }, {
        name: '여성',
        data: weekvalue(1) //[35, 41, 36, 26, 45, 48, 52] //
        }],
    chart: {type: 'bar',height: 350},
    plotOptions: {bar: {horizontal: false,columnWidth: '55%',endingShape: 'rounded'},},
    dataLabels: {enabled: false},
    stroke: {show: true,width: 2,colors: ['transparent']},
    xaxis: {categories: ['10대 미만', '10대', '20대', '30대', '40대', '50대', '60대 이상'],},
    fill: {opacity: 1},
    tooltip: {
        y: {formatter: function (val) {
            return val 
            }}
    }
};

var options2 = {
chart: {type: "area", height: 300, foreColor: "#ffffff", stacked: true,
dropShadow: {enabled: true, enabledSeries: [0], top: -2, left: 2, blur: 5,opacity: 0.06}},
colors: ['#4098f0'], //차트 색상 
stroke: {curve: "smooth",width: 3},
dataLabels: {enabled: false},
series: [
{name: 'the floating population', data:graph2()},//generateDayWiseTimeSeries(7, 2)},
// {name: 'second data', data: generateDayWiseTimeSeries(1, 18)}
],
markers: {size: 0, strokeColor: "#fff", strokeWidth: 3,
strokeOpacity: 1, fillOpacity: 1,hover: {size: 6}},
xaxis: {
    // type: "datetime", 
    axisBorder: {show: false}, axisTicks: {show: false},
    categories: ['01 Sep', '02 Sep', '03 Sep', '04 Sep', '05 Sep', '06 Sep', '07 Sep'],
    },
yaxis: {
    min : minvalue(),
    labels: {offsetX: 14,offsetY: -5},
    tooltip: {enabled: false}
},
grid: {padding: {left: 0,right: 10}},
tooltip: {x: {format: "dd MMM yyyy"},},
legend: {position: 'top', horizontalAlign: 'left'},
fill: { type: "solid", fillOpacity: 0.5}
};

var chart = new ApexCharts(document.querySelector("#timeline-chart"), options);
chart.render();

var chart2 = new ApexCharts(document.querySelector("#timeline-chart2"), options2); 
chart2.render();