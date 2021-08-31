		$(function () {
    $.getJSON('http://127.0.0.1:5000/data.json', function (data) {
        // Create the chart
        $('#container').highcharts('StockChart', {
            rangeSelector : {
                selected : 1
            },
            title : {
                text : 'My Sensor'
            },
            series : [{
                name : 'Value',
                data : data,
                tooltip: {
                    valueDecimals: 2}}]
                
            
        });
    });
        $.getJSON('http://127.0.0.1:5000/data1.json', function (data1) {
        // Create the chart
        $('#container1').highcharts('StockChart', {
            rangeSelector : {
                selected : 1
            },
            title : {
                text : 'My Sensor'
            },
            series : [{
                name : 'Value',
                data : data1,
                tooltip: {
                    valueDecimals: 2}}]
                
            
        });
    });
    
    
    
    
    
    
});





