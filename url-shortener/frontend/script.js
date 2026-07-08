const shortenBtn=document.getElementById("shortenBtn");

const result=document.getElementById("result");

const loading=document.getElementById("loading");

const shortUrl=document.getElementById("shortUrl");

const copyBtn=document.getElementById("copyBtn");

const openBtn=document.getElementById("openBtn");

shortenBtn.addEventListener("click",async()=>{

const url=document.getElementById("urlInput").value.trim();

if(url===""){

alert("Please enter a URL");

return;

}

loading.classList.remove("hidden");

result.classList.add("hidden");

const response=await fetch("http://127.0.0.1:5000/api/shorten",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
url:url
})

});

const data=await response.json();

loading.classList.add("hidden");

result.classList.remove("hidden");

shortUrl.value=data.short_url;

});

copyBtn.onclick=()=>{

navigator.clipboard.writeText(shortUrl.value);

copyBtn.innerHTML="Copied!";

setTimeout(()=>{

copyBtn.innerHTML=" Copy";

},1500);

}

openBtn.onclick=()=>{

window.open(shortUrl.value,"_blank");

}
