function resizeContentMain(){    
    
    let h = document.getElementById("normal-header").clientHeight;    
    let m = document.getElementById("main-content").clientHeight;
    let b = document.getElementById("footer").clientHeight;
    
    let height = window.innerHeight;

    console.log(h); // 66.5
    console.log(m);
    console.log(b); // 64    
    console.log(height);

    let difScrll = height - (h+m+b);
    if(difScrll > 0){
        console.log("xxx");
        console.log(difScrll);
        document.getElementById("main-content").style.height = (m+difScrll)+"px";
    }
    
}