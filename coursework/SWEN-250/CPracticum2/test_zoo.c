/*
 * Test suite for the four functions in the zoo module.
 */

#include <stdlib.h>
#include <stdio.h>

#include "memory.h"
#include "assert.h"
#include "zoo.h"

/*
 * Numbers for animal classes.
 */
#define MAMMAL		(0)
#define FALCON		(1)
#define REPTILE		(2)

/*
 * Numbers for animal species (unique within class).
 */

#define LION		(0)	/* MAMMAL */
#define ZEBRA		(1)	/* MAMMAL */
#define LINCOLN		(0)	/* FALCON */
#define CAESAR		(1)	/* FALCON */
#define SNAKE		(0)	/* REPTILE */
#define TURTLE		(1)	/* REPTILE */

/*
 * The test functions.
 */

static void test1() ;
static void test2() ;
static void test3() ;
static void test4() ;
static void test5() ;
static void test6() ;

int main(int argc, char *argv[]) {
	//set_test_mode(RUN_TO_TEST_FAILURE) ;
	set_test_mode(RUN_TO_ASSERT_FAILURE) ;

    int testnum;

    if (argc == 2){
        testnum = atoi(argv[1]); 
    }
    else {
        printf ("\nRun me as: \n");  
        printf ("./test_zoo <testNum>.\n");  
        printf ("Where <testNum> is upto what test you want to run.\n");  
        printf ("If <testNum> is 0, then I will test all\n\n");  
        exit(0);
    }
       //printf ("TESTNUM =%d. \n",testnum);


    if ((testnum >= 1 || testnum == 0)) {test1();} ;
    if ((testnum >= 2 || testnum == 0)) {test2();} ;
    if ((testnum >= 3 || testnum == 0)) {test3();} ;
    if ((testnum >= 4 || testnum == 0)) {test4();} ;
    if ((testnum >= 5 || testnum == 0)) {test5();} ;
    if ((testnum >= 6 || testnum == 0)) {test6();} ;

	summary() ;
}

/*
 * Requires add_animals()
 *
 * Adds one animal class and species to check 
 * and checks the memory allocator to ensure the correct number
 * of nodes hav been created.
 */
static void test1() {
    printf("\n*********************************************\n");
    printf("TEST1 - Add animal and check allocated count.\n");

	newtest("add_animals() once") ;
printf("----------------\n");

	printf("\nAdd 1 animal species to empty zoo collection\n") ;
	add_animals(MAMMAL, ZEBRA, 5) ;

	printf("Check 1 area allocated\n") ;
	assert(allocated_area_count() == 1) ;

   printf("\n*********************************************\n");
}
/*
 * Requires add_animals() & animal_count().
 *
 * Check animals are in the zoo with the correct counts.
 * Also checks the memory allocator to ensure the correct number
 * of nodes hav been created.
 */
static void test2() {
    printf("\n*********************************************\n");
    printf("TEST2 - Check for animal counts in zoo with one animal class and species.\n");

	newtest("animal_count()") ;
printf("----------------\n");
	printf("\nCheck the animal count is correct\n") ;
	assert(animal_count(MAMMAL, ZEBRA) == 5) ;
printf("----------------\n");

	printf("\nCheck for non-existent animal\n") ;
	assert(animal_count(MAMMAL, LION) == 0) ;
printf("----------------\n");

	printf("\nCheck 1 area allocated\n") ;
	assert(allocated_area_count() == 1) ;

    printf("\n*********************************************\n");
}

/*
 * Requires add_animals() & animal_count().
 *
 * Adds different class and species to zoo and checks for correct counts.
 * Also checks the memory allocator to ensure the correct number
 * of nodes hav been created.
 */
static void test3() {
    printf("\n*********************************************\n");
    printf("TEST3 - Add more animals of different class and species\n");
    
	newtest("multiple add_animals() and animal_count()") ;
printf("----------------\n");
	printf("\nAdd a 2nd animal species to the zoo collection\n") ;
	add_animals(FALCON, LINCOLN, 10) ;
	printf("\nCheck the animal count is correct\n") ;
	assert(animal_count(FALCON, LINCOLN) == 10) ;
printf("----------------\n");

	printf("\nAdd a 3rd animal species to the zoo collection\n") ;
	add_animals(REPTILE, SNAKE, 8) ;
	assert(animal_count(REPTILE, SNAKE) == 8) ;
printf("----------------\n");

	printf("\nCheck 3 areas allocated\n") ;
	assert(allocated_area_count() == 3) ;


    printf("\n*********************************************\n");
}

/*
 * Requires add_animals() & animal_count().
 *
 * Adds more animals to an existing class and species to zoo and checks for correct counts.
 * Also checks the memory allocator to ensure the correct number
 * of nodes hav been created.
 */
static void test4() {
    printf("\n*********************************************\n");
    printf("TEST4 - Add more animals for existing class and species\n");
    
printf("----------------\n");

	printf("\nAdd more of existing species\n");
	add_animals(FALCON, LINCOLN, 13) ;
	assert(animal_count(FALCON, LINCOLN) == 23) ;
printf("----------------\n");

	printf("\nCheck 3 areas allocated\n") ;
	assert(allocated_area_count() == 3) ;

printf("\n==========================================\n");
	printf("\nAdd animals to the zoo: 2 new items, 2 updated items\n") ;
	add_animals(REPTILE, TURTLE, 15) ;
	add_animals(REPTILE, SNAKE, 10) ;
	add_animals(FALCON, LINCOLN, 9) ;
	add_animals(MAMMAL, LION, 2) ;

printf("----------------\n");
    printf("\nChecking all animal counts correct.\n") ;
	assert(animal_count(MAMMAL, ZEBRA) == 5) ;
	assert(animal_count(MAMMAL, LION) == 2) ;
	assert(animal_count(FALCON, LINCOLN) == 32) ;
	assert(animal_count(FALCON, CAESAR) == 0) ;
	assert(animal_count(REPTILE, SNAKE) == 18) ;
	assert(animal_count(REPTILE, TURTLE) == 15) ;

printf("----------------\n");
	printf("\nCheck 5 areas allocated\n") ;
	assert(allocated_area_count() == 5) ;

   printf("\n*********************************************\n");
}

/*
 * Requires all previous tests HAVE PASSED and class_count()
 */
static void test5() {
    printf("\n*********************************************\n");
    printf("TEST5\n");
	newtest("totals by class") ;
    
printf("----------------\n");
	printf("\nChecking total of MAMMAL is correct\n") ;
	assert(class_count(MAMMAL) == 7) ;
printf("----------------\n");

	printf("\nChecking total of FALCON is correct\n") ;
	assert(class_count(FALCON) == 32) ;
printf("----------------\n");

	printf("\nChecking total of REPTILE is correct\n") ;
	assert(class_count(REPTILE) == 33) ;

    printf("\n*********************************************\n");
}

/*
 * Requires test5() passed and delete_collection().
 */
static void test6() {
    printf("\n*********************************************\n");
    printf("TEST6\n");
	newtest("delete zoo collection") ;

	printf("Closing zoo ...\n") ;
	close_zoo() ;

    printf("\nChecking all animal counts == 0 .\n") ;
	assert(animal_count(MAMMAL, ZEBRA) == 0) ;
	assert(animal_count(MAMMAL, LION) == 0) ;
	assert(animal_count(FALCON, LINCOLN) == 0) ;
	assert(animal_count(FALCON, CAESAR) == 0) ;
	assert(animal_count(REPTILE, SNAKE) == 0) ;
	assert(animal_count(REPTILE, TURTLE) == 0) ;
printf("----------------\n");

	printf("\nCheck no orphan storage. 0 areas allocated\n") ;
	assert(allocated_area_count() == 0) ;

    printf("\n*********************************************\n");
    printf("\n************** YOU DID IT! ******************\n");
    printf("\n*********************************************\n");

}
