function getlocation(){
    const p1 =document.getElementById("p1")
    if("geolocation" in navigator){
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                p1.textContent = "latitude" + latitude +  "" +"longitude" + longitude;
            }
        )
    }
}
