// JavaScript Document

var div = 1.5;

function onLoad()
{
	document.getElementById("background").onscroll = function(e)
	{	
		
		console.log(document.getElementById("background").scrollTop);
		//console.log((document.getElementById("scroller").scrollTop/2));
		//console.log((-4000-document.getElementById("scroller").scrollTop/100));
		
	}
}

function imageClick (fileName)
{ 
document.getElementById("largeImage").src = "images/gallery/"+ fileName +".jpg"; 
console.log("images/gallery/"+ fileName +".png"); 

}

txt = new Array();

txt[1] = "Streetview 1";
txt[2] = "Streetview 2";
//txt[3] = "Livingroom, Fire Place";
txt[4] = "Ceasarstone island contains gas cook top and gas oven. Elsewhere 2 sinks (1 prep), built-in dishwasher, built-in refrigerator w/icemaker, standalone stainless steel fume hood, under counter Marvel wine cooler. Built-in custom banquette breakfast nook and I-pad powered full home control centre. Slate coloured porcelain floors and indirectly lit valences.";
txt[5] = "Colour co-ordinated built-in Miele appliances. Appliance tower has a coffee/espresso maker, warming drawer, and a electric speed oven (combination microwave & convection oven).";
txt[6] = "Cathedral ceiling, extensive wood details, 2 wood framed sliding glass doors to 2 separate decks. Remote control see-thru gas fireplace, indirectly lit valences, built in sideboard.";
txt[7] = "Hallway to Kitchen";
txt[8] = "The Study: Cathedral ceiling, extensive wood details, easy access to front door for home office.";
txt[9] = "Main Entrance Interior";
txt[10] = "Main Entrance Exterior";
txt[11] = "Backyard 1";
txt[12] = "Backyard 2";
txt[13] = "Backyard 3";
txt[14] = "Backyard 4";
txt[15] = "Master Bathroom";

function changeText(n){
	document.getElementById("caption").innerHTML = txt[n];
	}