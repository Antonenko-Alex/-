for i:=1 to n do
begin
for j:=1 to m do
if j=1 then begin max:=b[i,j];min:=b[i,j]; end
else begin if b[i,j]>max then max:=b[i,j]; k:=j; if b[i,j]<min then min:=b[i,j]; l:=j;end;
tmp:=a[i,1];a[i,1]:=a[i,k]; a[i,k]:=tmp;
tmp:=a[i,m];a[i,m]:=a[i,l]; a[i,l]:=tmp;
end;
