function PlotBtc(){
  let year1_value = document.getElementById("year1");
  let year2_value = document.getElementById("year2");
  let year1=get_value_and_clear(year1_value);
  let year2=get_value_and_clear(year2_value);
   let data7 = {"year_start": year1, "year_end": year2};
  let dataJSON1 = JSON.stringify(data7);
  ajaxPostRequest("/BTC", dataJSON1, displayBTC)
}

function get_value_and_clear(input_obj) {
  let retVal = input_obj.value;
  input_obj.value = "";
  return retVal;
}

function PlotEth(){
  let year1_value = document.getElementById("year1");
  let year2_value = document.getElementById("year2");
  let year1=get_value_and_clear(year1_value);
  let year2=get_value_and_clear(year2_value);
  let data6 = {"year_start": year1, "year_end": year2};
  let dataJSON2 = JSON.stringify(data6);
  ajaxPostRequest("/ETH", dataJSON2, displayETH)
}

function Compare(){
  let year1_value = document.getElementById("year1");
  let year2_value = document.getElementById("year2");
  let year1=get_value_and_clear(year1_value);
  let year2=get_value_and_clear(year2_value);
  let data_comp={"year_start":year1,"year_end":year2};
  let dataJSON3 = JSON.stringify(data_comp);
  ajaxPostRequest("/compare",dataJSON3,display_compare)
  ajaxPostRequest("/compare1",dataJSON3,display_compare1)
}




function displayBTC(data0){
  let data12 = JSON.parse(data0);
  let s = data12[0]["name"];
  let f = data12[data12.length-1]["name"];
  let layout = {title: 'Bitcoin rate over the years <br>', grid: {rows: 1, columns: data12.length} };
  Plotly.newPlot("myDiv", data12, layout);
}

function displayETH(data09){
  let data1 = JSON.parse(data09);
  let s = data1[0]["name"];
  let f = data1[data1.length-1]["name"];
  let layout = {title: 'Ethereum rate over the years <br>', grid: {rows: 1, columns: data1.length} };
  Plotly.newPlot("myDiv", data1, layout);
}

function display_compare(datab){
  let dataa=JSON.parse(datab);
  let s = dataa[0]["name"];
  let f = dataa[dataa.length-1]["name"];
  let layout = {title: 'Comparison over the years <br>',barmode:"stack" , showlegend: true, grid: {rows: 1, columns: dataa.length} } ;
  Plotly.newPlot("myDiv", dataa, layout);
}
function display_compare1(datad){
  let datae=JSON.parse(datad);
  let s = datae[0]["name"];
  let f = datae[datae.length-1]["name"];
  let layout = {title: 'Comparison over the years <br>' , showlegend: true, grid: {rows: 1, columns: datae.length} } ;
  Plotly.newPlot("myDiv2", datae, layout);
}


// path is URL we are sending request
// callback function that JS calls when server replies
function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState===4&&this.status ===200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

// path is URL we are sending request
// data is JSON blob being sent to the server
// callback function that JS calls when server replies
function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState===4&&this.status ===200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}
