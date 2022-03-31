function openSubmenu(){
    if(document.getElementById("sub-menu-title").style.display === "inline"){
        document.getElementById("sub-menu-title").style.display = "none";
    }else{
        document.getElementById("sub-menu-title").style.display = "inline";
    }
}

function showLinkPopup(){    
    document.getElementById("mini-menu").style.display = "inline";
}

function hidePopupMiniMenu(){
    document.getElementById("mini-menu").style.display = "none";
}

function openSubMenuMobile(){
    if(document.getElementById("sub-menu").style.display === "inline"){        
        document.getElementById("sub-menu").style.display = "none";
    }else{        
        document.getElementById("sub-menu").style.display = "inline";
        document.getElementById("sub-menu").style.background = "#EB297B";
    }
}

function showEventList(){    
    document.getElementById("list-event-menu").style.display = "inline";
    document.getElementById("list-event-menu").style.background = "#4F4F4F";
}
function hidePopupListEvent(){
    document.getElementById("list-event-menu").style.display = "none";
}