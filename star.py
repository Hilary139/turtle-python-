from turtle import *
color('green', 'blue')
begin_fill()

while True:
    forward(150)
    left(170)
    # right(150)
    if abs(pos()) < 1:
        break
end_fill()
done()        