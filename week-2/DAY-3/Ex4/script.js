const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
    console.log(building.numberOfFloors);
    console.log(building.numberOfAptByFloor.firstFloor);
    console.log(building.numberOfAptByFloor.thirdFloor);
    console.log(building.nameOfTenants);

    const sarahRent = building.numberOfRoomsAndRent.sarah;
    const davidRent = building.numberOfRoomsAndRent.david;
    const danRent = building.numberOfRoomsAndRent.dan; 

    if(sarahRent + davidRent > danRent){
        building.numberOfRoomsAndRent.dan = 1200
    }
    console.log(danRent);