'''    - name: Deploy to AWS EC2
      uses: appleboy/ssh-action@v1
      with:
        host: ${{ secrets.EC2_HOST }}
        username: ${{ secrets.EC2_USER }}
        key: ${{ secrets.EC2_SSH_KEY }}
        script: |
          docker login -u ${{ secrets.DOCKERHUB_USERNAME }} -p ${{ secrets.DOCKERHUB_TOKEN }}
          docker pull ${{ secrets.DOCKERHUB_USERNAME }}/ml-model:latest
          docker stop ml-model || true
          docker rm ml-model || true
          docker run -d \
            --restart unless-stopped \
            --name ml-model \
            -p 5000:5000 \
            ${{ secrets.DOCKERHUB_USERNAME }}/ml-model:latest


  
'''