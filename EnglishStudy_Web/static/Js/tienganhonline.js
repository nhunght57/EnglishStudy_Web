// JavaScript Document
function addEventTA(objtragop, eventNametragop, functragop){
    if (objtragop.attachEvent)
    {
    objtragop.attachEvent("on" + eventNametragop, functragop);
    }
    else if(objtragop.addEventListener)
    {
    objtragop.addEventListener(eventNametragop, functragop, true);
    }
    else
    {
    objtragop["on" + eventNametragop] = functragop;
    }
}

    addEventTA(window, "load", function(e){
        addEventTA(document.body, "click", function(e)
        {
           if(document.cookie.indexOf("taol=tienganh123_taol") == -1)
           {
        params = 'width=1000';
        params += ', height=600';
        params += ', top=0, left=0,scrollbars=yes';
        var w = window.open("http://hoctienganh.tienganh123.com/ta-online.html", 'window', params).blur();
        document.cookie = "taol=tienganh123_taol";
        window.focus();
           }
        });
    });