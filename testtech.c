


/*
-----------------------------------------
Declaration des bibliotheques utilisees
-----------------------------------------
*/
#include <stdio.h>
#include <stdlib.h>

/*
-----------------------------------------
PROGRAMME PRINCIPAL
-----------------------------------------
*/

int	main(void) /*la fonction principale*/

{  


	int i=0;  /*déclarer et initialiser à 0 l'index i*/
	char	**str; /* pointeur vers pointeur de notre tableau de type char*/
	
	str = (char **)malloc(sizeof(char *) * 10);  /* allocation dynamique de la mémoire*/
	str[0] = "Ruben";      /*joueur numéro 1*/
	str[1] = "Pogba";	/*joueur numéro 2*/
	str[2] = "Benzema";	/*joueur numéro 3*/
	str[3] = "Mbappé";	/*joueur numéro 4*/
	str[4] = "Griezmann";	/*joueur numéro 5*/
	str[5] = "Lloris";	/*joueur numéro 6*/
	str[6] = "Kanté";	/*joueur numéro 7*/
	str[7] = "Giroud";	/*joueur numéro 8*/
	str[8] = "Varane";	/*joueur numéro 9*/
	str[9] = "Hakimi";	/*joueur numéro 10*/
	str[10] = NULL;	/*fin de contenu de tableau*/


	printf("La liste complète des joueurs : \n");  /*affichage de "La liste complète des joueurs*/
	
	while (str[i]) /*une boucle while pour parcourir le tableau*/
	{
	
	printf("%s\n", str[i]); /*afficher les noms des joueurs*/
		i++; /*incrémenter l'index i pour passer à l'affichage de nom du prochain joueur*/
	
	}
	
	while(str[i+1]) /*boucle while pour afficher le nom d'un seul joueur en donnant son numéro*/
	
	{
		i=0; /* initialiser l'index i afin d'éviter les erreurs*/
		printf("Donnez le numéro du joueur :\n"); /*afficher "Donnez le numéro du joueur*/
		scanf("%d",&i); /*scanf permettant de lire le numéro du joueur et l'affecter à l'index i*/
		
	if(i>10 || i<1) /* l'index i est limité en 1 et 10 inclus*/
	
		{
		
		printf("Joueur introuvable \n"); /* si i est supérieur à 10 ou inférieur à 1 le programme affiche "joueur introuvable*/
		return 0;

		}
	
		printf("Le joueur numéro %d : %s\n",i, str[i-1]); /*sinon il affiche le nom du joueur portant ce numéro*/
		return 0;
	
	}
	
}

