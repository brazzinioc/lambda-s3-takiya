### Convert JPG to Webp
Función Lambda para convertir imágenes JGP, PNG, JPEG a Webp.

Tiempo de ejecución: 2 mins
Memoria: 512 MB
Bucket Origen: takiya-process
Bucket Destino: takiya

### Built and deploy Image
Construcción y ejecución del contenedor.
```bash
    # contruye imagen
    docker build -t convert-jpg-to-webp .

    # asigna un tag
    docker tag convert-jpg-to-webp:latest 288219901735.dkr.ecr.us-east-2.amazonaws.com/convert-jpg-to-webp:latest

    # envia imagen a ECR (tener un usuario con acceso a ECR)
    docker push 288219901735.dkr.ecr.us-east-2.amazonaws.com/convert-jpg-to-webp
```
