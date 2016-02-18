function [mq,mr]=gs2(a)
% Ortogonalizacion de Gram Schmidt
% Algoritmo estandar
[m,n]=size(a);
mq(:,1)=a(:,1)/norm(a(:,1));
mr=zeros([n,n]);
mr(1,1)=norm(a(:,1));
for k=2:n,
   q=mq(:,1:k-1);
   q=eye(m)-mq*mq';
   mq(:,k)=q*a(:,k);
   mr(k,k)=norm(mq(:,k));
   mq(:,k)=mq(:,k)/mr(k,k);
   for j=1:k-1,
        mr(j,k)=mq(:,j)'*a(:,k);
   end 
end