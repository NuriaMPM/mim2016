function [mq,mr]=gs2(a)
% Ortogonalizacion de Gram Schmidt
% Algoritmo estandar
[m,n]=size(a);

% Primera columna de la matriz Q:
mq(:,1)=a(:,1)/norm(a(:,1));

% primera columna de la matriz R:
mr=zeros([n,n]);
mr(1,1)=norm(a(:,1));

% algoritmo para las n-1 restantes columnas:
for k=2:n,
   q=mq(:,1:k-1);           % vector q anterior, extraido de Q
   q=eye(m)-mq*mq';      
   mq(:,k)=q*a(:,k);        % vector q~ perpendicular al a
   mr(k,k)=norm(mq(:,k));   % rellenamos el coeficiente k,k de la R 
   mq(:,k)=mq(:,k)/mr(k,k); % vector q normalizado
   % El resto de columna de R son productos escalares de Q y A    
   for j=1:k-1,
        mr(j,k)=mq(:,j)'*a(:,k);
   end 
end