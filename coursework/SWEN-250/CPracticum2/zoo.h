/*
 * Maintain quantitys of animals in the zoo.
 *
 * Animals have a class (mammal, bird, etc.) and a species,
 * both encoded as unsigned integers.
 *
 * The species numbers are only guaranteed to be unique to a given class
 * (that is, a lion could be species 1 in mammal and a turtle could be
 * species 1 in reptile).
 */

/*
 * Interface to the zoo animal tracking program.
 */

#ifndef ZOO_H
#define ZOO_H

/*
 * Add <number> new animals of the given <class> and <species> and add
 * these to the existing collection. That is, increment the zoo's
 * record of quantity of this animal by <number>.
 */
void add_animals(unsigned class, unsigned species, unsigned number) ;

/*
 * Return the count of the given animal (<class> and <species>) held
 * by the zoo.
 */
unsigned animal_count(unsigned class, unsigned species) ;

/*
 * Return the number of animals belonging to the given <class>
 * held by the zoo.
 */
unsigned class_count(unsigned class) ;

/*
 * Close the zoo - at the end, the zoo has no animals.
 */
void close_zoo() ;

#endif
