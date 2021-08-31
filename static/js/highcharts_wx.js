var timeStamp = []; //감지된 시간 저장 배열 
var detectedObjects = []; //감지된 사람 저장 배열 
var now = []; //사회적 거리두기를 어긴 사람 배열 
//파일을 백그라운드에서 받기위한 Ajax 
$(document).ready(function() { 
function getLog() { 
  $
  .ajax({ 
  url : '/live-data3', // 읽어올 파일의 경로 
dataType : 'text',         // 읽어온 파일을 활용하기 위한 형태 
success : function(data) { // ajax 성공시, 

var count = 0; 
var allRow = data.split(","); // 띄어쓰기 단위로 구분 

//최근 60열의 데이터만 저장 
//한페이지에 표시되는 데이터 20개
if (allRow.length > 200) { 
allRow = allRow.slice(-120,); 
} 
//console.log(allRow)
//console.log("printallFow",allRow)
var line = 0; //저장된 데이터의 열 개수를 저장하기 위한 변수 
for (var singleRow = 0; singleRow < allRow.length; singleRow++) { 
    if (singleRow % 2 == 0)
    {
        collapse = allRow[singleRow]//센서값
        textLine = parseFloat(collapse); // 그래프 파싱을 위해 Int형 변환 
        detectedObjects.push(textLine) 
        console.log("object",textLine); 
    }
    else
    {
        collapse = allRow[singleRow]
        textIn=collapse
        timeStamp.push(textIn) 
        console.log("time",textIn)
    }

 
} 
 





  setTimeout(getLog, 60000); // refresh every 60 seconds 
} 
}); 
} 
getLog(); 
 
// 
Highcharts.chart('data-container', { 
chart : { 
type : 'column',    // 베이직(곡선형) 그래프 
        zoomType : 'x', // x축 방향으로 그래프 그리기 가능 
        gridLineWidth : 3, // 선 굵기 

events : {         // 차트 이벤트 
load : function() { 
var series = this.series[0]; // Series의 index 0을 대입 
var i = 0; 
 
/* 
* 1초단위로 데이터를 받아서 동적 그래프에 그려주기 위한 Interval함수 
*/ 

setInterval(function() { 
 
x = timeStamp[i]; // timestamp 
y1 = detectedObjects[i]; // detectedObjects 
i++; // index값 증가 
 
//console.log("X Data insert : " + y1); 
series.addPoint([ x, y1 ], true, true); // series에 데이터 추가 
 
}, 1000); // interval end 
}         // load     end 
} // events   end 
},         // charts   end 
 
title : { 
text : 'Vibration Data graph' // 그래프 이름 
}, 
 
subtitle : { 
 
text : 'Vibration Data' // 서브 타이틀 
}, 
 
tooltip : { 
crosshairs : [ false, true ], // 특정 포인트를 짚으면 [x, y] 축 둘중 하나의 축에 대한 라인이 생긴다. 
valueDecimals : 2 // long형 데이터를 받기 위함 
}, 
 
xAxis : { 
categories : timeStamp ,
//type : 'string' // x축 단위 

}, 
 
yAxis : { 
labels : { 
formatter : function() { 
return this.value ;     // y축 단위 
} // formatter end 
}, // labels    end 
type : 'column', // 선형 그래프 
gridLineWidth : 1 // 선 굵기 
}, 
 
/* 
* 데이터 -> 그래프 삽입 부분 
*/ 
series : [ { 
 
data : (function() { 
var data = [], i; // 보여질 데이터, 반복문 인자 
for (i = -19; i <= 0; i++) { 
data.push({ x : detectedObjects[i] + i * 1000 
}); 
} 
return data; 
})(), 
lineWidth : 1,    // 라인 넓이 
name : 'Vibration Data'            // 데이터 이름 
} 
 
] ,

}); 


}); 

