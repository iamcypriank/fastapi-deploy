from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Surprise 😈</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,Helvetica,sans-serif;
}

body{
    background:linear-gradient(135deg,#0f172a,#1e293b);
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:hidden;
}

.card{
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(10px);
    padding:60px;
    border-radius:20px;
    text-align:center;
    box-shadow:0 20px 40px rgba(0,0,0,.35);
}

button{
    padding:18px 36px;
    border:none;
    border-radius:12px;
    font-size:20px;
    cursor:pointer;
    background:#22c55e;
    color:white;
    transition:.25s;
}

button:hover{
    transform:scale(1.05);
}

#message{
    display:none;
    margin-top:35px;
    font-size:48px;
    font-weight:bold;
    color:#ff4757;
    animation:pop .5s ease;
}

@keyframes pop{
    from{
        transform:scale(.2);
        opacity:0;
    }
    to{
        transform:scale(1);
        opacity:1;
    }
}

.confetti{
    position:fixed;
    width:10px;
    height:10px;
    top:-20px;
    animation:fall linear forwards;
}

@keyframes fall{
    to{
        transform:translateY(110vh) rotate(720deg);
        opacity:0;
    }
}
</style>

</head>
<body>

<div class="card">
    <button onclick="surprise()">
        🎁 I have a Surprise for You
    </button>

    <div id="message">
        PADH LE BETICHOD 📚
    </div>
</div>

<script>

function randomColor(){
    const colors=[
        "#ff4757",
        "#2ed573",
        "#1e90ff",
        "#ffa502",
        "#e84393",
        "#70a1ff",
        "#7bed9f",
        "#ff6b81"
    ];

    return colors[Math.floor(Math.random()*colors.length)];
}

function confetti(){

    for(let i=0;i<220;i++){

        const piece=document.createElement("div");
        piece.className="confetti";

        piece.style.left=Math.random()*100+"vw";
        piece.style.background=randomColor();

        const size=6+Math.random()*12;

        piece.style.width=size+"px";
        piece.style.height=size+"px";

        piece.style.animationDuration=(2+Math.random()*3)+"s";

        document.body.appendChild(piece);

        setTimeout(()=>{
            piece.remove();
        },5000);
    }
}

function surprise(){

    document.querySelector("button").style.display="none";

    confetti();

    setTimeout(()=>{
        document.getElementById("message").style.display="block";
    },1000);

}

</script>

</body>
</html>
"""