<html>
<body>

<h1>Team 10: Koch SnowFlake</h1>

<script>
(() => {
    var limiter = prompt ("please imput your number")
    if (limiter>6){
      prompt ("input higher than 6 may take a while")}
    const canvas = document.createElement('canvas')
    document.body.appendChild(canvas)

    const context = canvas.getContext('2d')
    const width = canvas.width = 700
    const height = canvas.height = 500

    const startingPoints = {
        p1: {
            x: 0,
            y: -150
        },
        p2: {
            x: 150,
            y: 100
        },
        p3: {
            x: -150,
            y: 100
        }
    }
    context.translate(.5 * width, .5 * height)

    const koch = (a, b, limit = limiter) => {
        let [dx, dy] = [b.x - a.x, b.y - a.y]
        let dist = Math.sqrt(dx * dx + dy * dy)
        let unit = dist / 3
        let angle = Math.atan2(dy, dx)
        let p1 = {
            x: a.x + dx / 3,
            y: a.y + dy / 3
        }
        let p3 = {
            x: b.x - dx / 3,
            y: b.y - dy / 3
        }
        let p2 = {
            x: p1.x + Math.cos(angle - Math.PI / 3) * unit,
            y: p1.y + Math.sin(angle - Math.PI / 3) * unit
        }
         if (limit > 0) {
        	// Decrease limit each time it's called
            koch(a, p1, limit - 1)
            koch(p1, p2, limit - 1)
            koch(p2, p3, limit - 1)
            koch(p3, b, limit - 1)
        } else {
            context.beginPath()
            context.moveTo(a.x, a.y)
            context.lineTo(p1.x, p1.y)
            context.lineTo(p2.x, p2.y)
            context.lineTo(p3.x, p3.y)
            context.lineTo(b.x, b.y)
            context.stroke()
        }
    }
    koch(startingPoints.p1, startingPoints.p2)
    koch(startingPoints.p2, startingPoints.p3)
    koch(startingPoints.p3, startingPoints.p1)

 })()
</script>

</body>
</html>
