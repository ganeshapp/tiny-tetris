import time,random,sys;import curses as h;w=h.initscr();h.noecho();h.cbreak()   #
rs,cs,m,s,e,p,a,q=20,10,5,300,{0:"  ",1: "# "},[[[1,1],[1,1]],[[0,1,0],[1]*3,[0]#
*3],[[1,0,0],[1]*3,[0]*3],[[0,0,1],[1]*3,[0]*3],[[1,1,0],[0,1,1],[0]*3],[[0,1,1]#
,[1,1,0],[0]*3],[[0]*4,[1]*4,[0]*4,[0]*4]],range,len;cu,b,f,t=p[random.randint(0#
,6)],[[0]*cs for r in a(rs)],False,True;y,ro,co,cr,l,d,n=lambda z,x,y,e=e:e[z[x]#
[y]],0,cs//2,0,1,s,p[random.randint(0,6)];w.nodelay(t);w.keypad(t);h.curs_set(f)#
A,B,sw=list,zip,{'U':'if not k(ro,co,A(B(*cu[::-1]))):cu=A(B(*cu[::-1]))','D':  #
'm_d();ro+=1','L':'if not k(ro,co-1,cu):co-=1','R':'if not k(ro,co+1,cu):co+=1'}#
exec(('def k(ro,co,se):\n for(r,c)in[(r,c)for c in a(q(cu))for r in a(q(cu))]:' #
'\n  if se[r][c]>0 and(not(0<=ro+r<rs and 0<=co+c<cs)or b[ro+r][co+c]>0):return'#
' t\ndef m_d():\n global ro,co,cu,n,l,d\n if(k(ro+1,co,cu)and ro<1 and sys.exit'#
'())or k(ro+1,co,cu):\n  for(r,c)in[(r,c)for c in a(q(cu))for r in a(q(cu))]:\n'#
'   if ro+r in a(rs)and co+c in a(cs)and cu[r][c]>0:b[ro+r][co+c]=cu[r][c]\n  c'#
'u,n,ro,co,d=n,p[random.randint(0,6)],-1,cs//2,s+m-l*m\n  for i in[j for j in a'#
'(rs)if sum(b[j])>9]:b[1:i+1]=b[:i];b[0],l=[0]*cs,l+1\ntry:\n while True:\n  o,'#
'z=a(q(n)),a(q(cu));u=[(r,c)for c in z for r in z];time.sleep(0.001)\n  for(r,c'#
')in[(r,c)for c in a(cs)for r in a(rs)]:w.addstr(r,c*q(e),y(b,r,c))\n  for(r,c)'#
'in[(r,c)for(r,c)in u if cu[r][c]==1]:w.addstr(ro+r,(co+c)*2,y(cu,r,c))\n  for('#
'r,c)in[(r,c)for c in o for r in o]:w.addstr(r,22+c*2,y(n,r,c)+"    ")\n  try:c'#
'r=(cr+1)%d;ch=w.getkey();exec(sw[ch[4:5]]);raise\n  except:exec("if cr==0:m_d('#
');ro+=1");w.addstr(rs,0,"="*19+"\\nlevel: "+str(l))\nexcept:h.echo();w.keypad('#
'f);h.nocbreak();h.endwin();print("score: "+str(l))'))# TINY TETRIS by NICK PAZ #