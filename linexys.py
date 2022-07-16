def lineXYS(sx,sy,ex,ey):#求两点间直线所有坐标值
    xys = []
    if sx==ex:
        step = 1
        if sy>ey:
            step = -1
        for y in range(sy,ey,step):
            xys.append([sx,y])
    elif sy==ey:
        step = 1
        if sx>ex:
            step = -1
        for x in range(sx,ex,step):
            xys.append([x,sy])
    else:
        xline = 0
        if sx<ex:
            xline = int(ex-sx)
        else:
            xline = int(sx-ex)
        yline = 0
        if sy<ey:
            yline = int(ey-sy)
        else:
            yline = int(sy-ey)
        if xline>=yline:
            if sx<ex:
                for x in range(sx,ex):
                    if sy<ey:
                        y = int((x-sx)*(yline*3)/(xline*3)+sy)
                        xys.append([x,abs(y)])
                    else:
                        y = int((x-sx)*(yline*3)/(xline*3)-sy)
                        xys.append([x,abs(y)])
            else:
                for x in range(sx,ex,-1):
                    if sy<ey:
                        y = int((sx-x)*(yline*3)/(xline*3)+sy)
                        xys.append([x,abs(y)])
                    else:
                        y = int((sx-x)*(yline*3)/(xline*3)-sy)
                        xys.append([x,abs(y)])
        else:
            if sy<ey:
                for y in range(sy,ey):
                    if sx<ex:
                        x = int((y-sy)*(xline*3)/(yline*3)+sx)
                        xys.append([abs(x),y])
                    else:
                        x = int((y-sy)*(xline*3)/(yline*3)-sx)
                        xys.append([abs(x),y])
            else:
                for y in range(sy,ey,-1):
                    if sx<ex:
                        x = int((sy-y)*(xline*3)/(yline*3)+sx)
                        xys.append([abs(x),y])
                    else:
                        x = int((sy-y)*(xline*3)/(yline*3)-sx)
                        xys.append([abs(x),y])
    return xys
