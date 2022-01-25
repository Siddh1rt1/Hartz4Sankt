
const a = ['2019Okt',	'2019Nov',	'2019Dez',	'2020Jan',	'2020Feb',	'2020Mär',	'2020Apr',	'2020Mai',	'2020Jun',	'2020Jul',	'2020Aug',	'2020Sep',	'2020Okt',	'2020Nov',	'2020Dez',	'2021Jan',	'2021Feb',	'2021Mär',	'2021Apr',	'2021Mai',	'2021Jun',	'2021Jul',	'2021Aug',	'2021Sep'];
const labels = a;

const mylive = document.getElementById("bory").innerHTML;
const mylove = document.getElementById("story").innerHTML;
const strArray = JSON.parse(mylove.replaceAll("'", "\""));
ame =  strArray[0]+" "+strArray[1];
const numbers = strArray.map(x => Number(x));

console.log("mooooon"+ame);
const bumbers = numbers.slice(4);
console.log("hyes"+numbers);



const data = {
  labels: labels,
  datasets: [{
    label: "Hartz4Sanktionen_"+ame+" in Prozent",
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    data: bumbers,

  }
  ,
  ],

};

const config = {
  type: 'line',
  data: data,
  options: {}
};
const myChart = new Chart(
  document.getElementById('myChart'),
  config
);



console.log(a);
var glolabel = 0;
d3.csv("/data/data.csv", function(data) {
var str = str(data);  
str.split("19");
console.log(str);
  
});
console.log("hello");
const z = document.getElementById("story").innerHTML;
console.log(z);
console.log("log_2");
