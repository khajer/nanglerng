function openSubmenu(){
    if(document.getElementById("sub-menu-title").style.display === "inline"){
        document.getElementById("sub-menu-title").style.display = "none";
    }else{
        document.getElementById("sub-menu-title").style.display = "inline";
    }
}

function showLinkPopup(){    
    if(document.getElementById("mini-menu").style.display === "inline"){        
        document.getElementById("mini-menu").style.display = "none";
    }else{        
        document.getElementById("mini-menu").style.display = "inline";
    }
}

function hidePopupMiniMenu(){
    document.getElementById("mini-menu").style.display = "none";
}