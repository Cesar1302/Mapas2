gmt gmtset MAP_FRAME_AXES WesN
gmt gmtset MAP_FRAME_TYPE fancy+
gmt gmtset MAP_FRAME_WIDTH 0.15
gmt grdmask -RTMAX.grd tlp.gmt -Gtmasktlp.grd -NNaN/NaN/1
gmt grdmath TMAX.grd tmasktlp.grd MUL = tmaxtlp.grd
gmt grdsample output_topo.grd -Gtopografia.grd -R-99.45/-99/19.05/19.4 -I0.1m -V -r
gmt grdsample tmaxtlp.grd -Gmaximatlp.grd -R-99.45/-99/19.05/19.4 -I0.1m -V -r
gmt grdimage maximatlp.grd -Ctemperatura.cpt -JM30 -R-99.45/-99/19.05/19.4 -Itopografia.grd -B0 -P -K > tlpmax.ps -Q
gmt gmtset PS_MEDIA=A0
gmt pscoast -R-99.45/-99/19.05/19.4 -W0.02/40/40/120 -N1/0.03c,red -JM -Df -Lf-99.29/19.09/19.0/10k+l -Tdg-99.05/19.25+w3c+f3+lW,E,S,N -P -O -K --PS_MEDIA=A0 >> tlpmax.ps
gmt psxy -R -J -O  cirvialtlp.gmt  -W0.6,black, -K >> tlpmax.ps
gmt psscale -D1.2c/8c/13c/0.5c -Ctemperatura.cpt -Ba2 -P -O -K >> tlpmax.ps
gmt pstext tlp.txt -R-99.45/-99/19.05/19.4 -JM  -: -Dj0.2/0.3 -P -O -V -K  >> tlpmax.ps
gmt psxy -R -J -O   tlp.gmt  -W2,black, >> tlpmax.ps
gmt psconvert -A -Tj -P tlpmax.ps
convert -composite tlpmax.jpg  SGIRPC.png -geometry +1550+100 tlpmax.jpg