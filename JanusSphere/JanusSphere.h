#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "JanusSphere.generated.h"

UCLASS()
class YOURPROJECT_API AJanusSphere : public AActor
{
    GENERATED_BODY()
    
public:    
    // Sets default values for this actor's properties
    AJanusSphere();

protected:
    // Called when the game starts or when spawned
    virtual void BeginPlay() override;

public:    
    // Called every frame
    virtual void Tick(float DeltaTime) override;

    // Function to control rotation
    void RotateSphere(float DeltaTime);

    // Components
    UPROPERTY(VisibleAnywhere)
    UStaticMeshComponent* SphereMesh;

    // Rotation speed in degrees per second
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Janus Sphere Properties")
    float RotationSpeed;
};

