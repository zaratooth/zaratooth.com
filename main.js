function CircleClick( toShow ) {

    console.log("clicked");
    
    $(".project-content").hide();        
    $("#"+toShow).show("500", "swing");   
}

function OnLoad(){
    
    /*$(".content-block").css({
        opacity : 1,
        minHeight : $(window).height() - 200 + "px"
    });*/
    
}