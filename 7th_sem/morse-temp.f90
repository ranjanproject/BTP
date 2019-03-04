!!!!!to be included: Expectation values as a function of time: this is done
module cnst
implicit real*4(a-h,o-z)
complex ai
parameter(pi = acos(-1.0))
parameter(ai = cmplx(0.0,1.0))
parameter(alpha = 1.0)
parameter(p0=0.0)
parameter(x0=3.0)
parameter(de=8.0)
parameter(emass=1.0)
parameter(dt=0.2)
parameter(nx=1024)
parameter(istep=1000)
complex psi0,psi1,psi2,psiinitial
allocatable::psi0(:),psi1(:),psi2(:),psiinitial(:)
character*4 scri
character*64 outran
end module cnst

program tdqm1d
use cnst
implicit real*4(a-h,o-z)
dimension vx(nx),x(nx)
complex comm,ftmp,auto,auto1
allocatable::comm(:),ftmp(:),akx(:),auto(:),homega(:)
open(unit=21,file='test.txt')
!open(unit=21,file='pot.out')
open(unit=22,file='wav0.out')
open(unit=23,file='wav1.out')
open(unit=24,file='test2.txt')

allocate(psi0(nx),psi1(nx),psi2(nx),akx(nx),psiinitial(nx))
!!!!!!!x-grid
xmin=0.5
xmax=25.0
dx=(xmax-xmin)/(nx-1)
do i=1,nx
 x(i)=xmin+(i-1)*dx
enddo

!potential 
omega=1.0
const=sqrt(1.0/(2.0*de))
do i=1,nx
 !vx(i)=de*(1.0-exp(-const*(x(i)-3.0)))**2
 write(21,*) x(i)!,vx(i)
enddo
!stop
call system("python potential.py")
do i=1,nx
   read(24,*) vx(i)
end do
do i=1,nx
   write(*,*) vx(i)
end do
!!!!Initial wavepacket
wnorm= (alpha/pi)**0.25
do i=1,nx
 psi0(i)=wnorm*(exp(ai*p0*(x(i)-x0)))*exp(-alpha*(x(i)-x0)**2/2.0)
 psisq = psi0(i)*conjg(psi0(i))
 write(22,*) x(i), psisq
enddo
psiinitial=psi0
!!!!!

!!!!Calculate k
dk=2.0d0*pi/(dfloat(nx)*dx)
i2=nx/2+1
do i=1,nx
   ak=(i-1)*dk
    if(i.gt.i2) ak=-(nx+1-i)*dk
   akx(i)=ak
end do

!!!!!at later times
Print*,'Enter nt'
read*,nt
allocate(ftmp(nx),comm(4*nx+15),auto(nt),homega(nt))
do it=1,nt

!potential
do i=1,nx
 psi1(i)=exp(-ai*vx(i)/2.0*dt)*psi0(i)
enddo

!kinetic
call fft(psi1,nx,+1)
do i=1,nx
 psi1(i)=exp(-ai*akx(i)*akx(i)*dt/(2.0*emass))*psi1(i)
enddo
call fft(psi1,nx,-1)
psi1=psi1/real(nx)

!potential
do i=1,nx
 psi1(i)=exp(-ai*vx(i)/2.0*dt)*psi1(i)
enddo

!!!!Expectation value of position
expos=0.0
do i=1,nx
 expos=expos+psi1(i)*x(i)*conjg(psi1(i))*dx
enddo
write(120,*)(it-1)*dt,it,expos

!!!!Expectation value of momentum
ftmp=psi1
call fft(ftmp,nx,+1)
do i=1,nx
 ftmp(i)=-akx(i)*ftmp(i)
enddo
call fft(ftmp,nx,-1)
ftmp=ftmp/real(nx)
exmom=0.0
do i=1,nx
 exmom=exmom+conjg(psi1(i))*ftmp(i)*dx
enddo
write(121,*)(it-1)*dt,exmom

!!!!Autocorrelation function
auto1=0.0
do i=1,nx
auto1=auto1+conjg(psiinitial(i))*psi1(i)*dx
enddo
auto(it)=auto1
write(122,*)(it-1)*dt,it,abs(auto(it))

do i=1,nx
 psisq = psi1(i)*conjg(psi1(i))
 if (mod(it,istep).eq.0) then
 write(outran,1161) it,p0
1161    format('npack.',i4.4,'.',f5.2)
 open(unit=16,file=outran,form='formatted',status='unknown')
 write(16,*)x(i),psisq
 endif
end do

do i=1,nx
 psi0(i)=psi1(i)
end do

if (mod(it,istep).eq.0) then
  call wrscri('scri',it)
endif

end do

end program tdqm1d



subroutine wrscri(scri,nstep)
implicit real*4 (a-h,o-z)
character*4 scri
open(unit=70,file='movie.inp')

write(70,*)'set title "time=',nstep*0.1,'"'
write(70,*)'set xrange [-2.5:2.5]'
write(70,25)nstep
write(70,*)'pause -1'
25    format('plot' '"fort.',i0, '"' 'w l,' '"pot.out"  &
       using 1:2    w l')
return
end


