#include "JanusSphere.h"

// Sets default values
AJanusSphere::AJanusSphere()
{
    // Set this actor to call Tick() every frame.  
    PrimaryActorTick.bCanEverTick = true;

    // Create and set up the mesh component
    SphereMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("SphereMesh"));
    RootComponent = SphereMesh;

    // Initialize variables
    RotationSpeed = 90.0f; // Default rotation speed to 90 degrees per second
}

// Called when the game starts or when spawned
void AJanusSphere::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void AJanusSphere::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Rotate the sphere
    RotateSphere(DeltaTime);
}

// Rotate the sphere based on RotationSpeed
void AJanusSphere::RotateSphere(float DeltaTime)
{
    FRotator NewRotation = FRotator(0.f, RotationSpeed * DeltaTime, 0.f);
    FQuat QuatRotation = FQuat(NewRotation);
    SphereMesh->AddLocalRotation(QuatRotation, false, 0, ETeleportType::None);
}

