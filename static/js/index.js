

console.log("1");

const a = ['2019Okt',	'2019Nov',	'2019Dez',	'2020Jan',	'2020Feb',	'2020Mär',	'2020Apr',	'2020Mai',	'2020Jun',	'2020Jul',	'2020Aug',	'2020Sep',	'2020Okt',	'2020Nov',	'2020Dez',	'2021Jan',	'2021Feb',	'2021Mär',	'2021Apr',	'2021Mai',	'2021Jun',	'2021Jul',	'2021Aug',	'2021Sep'];
const labels = a;
const mylive = document.getElementById("bory").innerHTML;
test = mylive.slice(2,-2);
const real=test.split(';');

console.log("2");
const mylove = document.getElementById("story").innerHTML;
console.log("3");
ame =  mylove.split(",");


console.log("ame=" +ame[0])
const strArray = JSON.parse(mylove.replaceAll("'", "\""));

const numbers = strArray.map(x => Number(x));
const bumbers = numbers.slice(4);

real.shift();
real.shift();

tre = document.getElementById("story").innerHTML;

const ntre = tre;

tre=tre.replace(',','');
tre=tre.replaceAll("'" ,'');
tre=tre.replaceAll("[" ,'');
tre=tre.replaceAll("]" ,'');
const num=tre.split(";");
hello=num[0];
console.log(hello);
num.shift();
const newne=num;

newne.shift();

const data = {
  labels: real,
  datasets: [{
    label: "Hartz4Sanktionsquote von "+hello+" in Prozent pro ELB",
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    data: newne,

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
