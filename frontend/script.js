fetch('http://127.0.0.1:5555/firstapi')
    .then((res)=>{
        return res.json()
    })
    .then((data)=>{
        console.log(data)
    })