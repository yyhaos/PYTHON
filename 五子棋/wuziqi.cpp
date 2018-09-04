#include<bits/stdc++.h>
using namespace std;
int maze[15][15];
int xx[8]={1,1,0,-1,-1,-1,0,1};
int yy[8]={0,-1,-1,-1,0,1,1,1};
int dp[10000000+5];
void draw()
{

    for(int k=1;k<=20;k++)
    for(int i=1;i<=10000000;i++)
    {
        dp[i]=dp[i-1]+dp[i];
    }
    system("cls");
    for(int i=1;i<=13;i++)
    {
        for(int j=1;j<=13;j++)
        {
            if(maze[i][j]==0)
                printf("Ê®");
            else if(maze[i][j]==1)
                printf("©–");
            else
                printf("¨€");
        }
        printf("\n");
    }
}

int down(int i,int j,int type)
{
    bool judge(int i,int j,int type);
    maze[i][j]=type;
    draw();
    return judge(i,j,type);
}
int len[10],tx,ty;
int judge(int gx,int gy,int type)
{

    memset(len,0,sizeof(len));
    for(int i=0;i<8;i++)
    {
        for(int k=1;k<=5;k++)
        {
            tx=gx+k*xx[i];
            ty=gy+k*yy[i];
            if(tx<=13 && tx>=1 && ty<=13 && ty>=1)
            {
                if(maze[tx][ty]==type)
                {
                    //printf("%d-%d-%d-%d\n",tx,ty,maze[tx][ty],type);
                    len[i]++;
                }
                else
                    break;
            }
            else
                break;
        }
    }
    for(int i=0;i<=3;i++)
    {
        //printf("%d : %d-%d\n",i,len[i],len[i+4]);
        if(len[i]+len[i+4]>=4)
            return type;
    }
    return 0;
}



int main ()
{
    int flag;
    while(1)
    {
        flag=0;
        memset(maze,0,sizeof(maze));
        printf("New round?\n");
        char t;
        scanf("%c",&t);
        if(t=='N')
            break;
        //int tx,ty;
        while(1)
        {
            if(flag!=0)
                break;
            printf("player 1 ©–\n");
            scanf("%d %d",&tx,&ty);
            while(maze[tx][ty]>0)
            {
                printf("player 1 retry ©–\n");
                scanf("%d %d",&tx,&ty);
            }
            flag=down(tx,ty,1);

            if(flag!=0)
                break;
            printf("player 2 ¨€\n");
            scanf("%d %d",&tx,&ty);
            while(maze[tx][ty]>0)
            {
                printf("player 2 retry ¨€\n");
                scanf("%d %d",&tx,&ty);
            }
            flag=down(tx,ty,2);

        }
        printf("%d is winner\n",flag);
    }
    return 0;
}
