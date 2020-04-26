
fpr=800; 
N=2000; 
f_syg=[100 270 320 399]; 
A_syg=[1 2 3 4]; 
Ts=1/fpr;
t=[0:Ts:(N-1)*Ts];

s1=A_syg(1)*cos(2*pi*f_syg(1)*t); 
s2=A_syg(2)*cos(2*pi*f_syg(2)*t); 
s3=A_syg(3)*cos(2*pi*f_syg(3)*t); 
s4=A_syg(4)*cos(2*pi*f_syg(4)*t); 

syg=s1+s2+s3+s4;

subplot(2,1,1);
plot(t,syg);
xlabel('Czas [s]');
title('Sygnal')

subplot(2,1,2);
ffts=abs(fft(syg,N));
df=fpr/N;
f=[0:df:(N-1)*df];
stem(f,ffts);
xlabel('Czestotliwosc [Hz]');
title('Charakterystyka amplitudowa')

