class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        M=len(squares)
        if M==1:
            return squares[0][1]+0.5*squares[0][2]

        total_area=sum([square[2]**2 for square in squares])

        squares.sort(key=lambda square: square[1])

        minY,maxY=squares[0][1],max([square[1]+square[2] for square in squares])

        l,r=minY,maxY
        maxTopBelow=True
        while r-l>1e-5:
            #print(l,r)
            maxTopBelow=True
            maxTop=-float('inf')
            MID=(l+r)/2
            area_below=0
            for square in squares:
                x,y,sz=square[0],square[1],square[2]
                if y>=MID: break
                width=sz
                top=min(MID, y+sz)
                maxTop=max(maxTop, y+sz)
                if y+sz>=MID: maxTopBelow=False
                bottom=y
                height=top-bottom
                area_below+=width*height
            #print(MID, area_below, maxTop, abs(area_below-total_area/2))

            if area_below<total_area/2:
                l=MID
            else:
                r=MID
        return r if not maxTopBelow else maxTop

