#define _LARGEFILE64_SOURCE /*See feature_test_macros(7)*/
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <ext2fs/ext2_fs.h>
#include <math.h>
#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define BASE_OFFSET 1024  /* location of the super-block in the first group */

void superblock(int fd);
struct ext2_super_block sblite(int fd);
int block_off(int block_size);
int block(int block_size, int num);
void group_descriptor(int fd);
struct ext2_group_desc group_desc(int fd, int i);
void block_bitmap(int fd, int gno);
void inode_bitmap(int fd, int gno);
void inode_table(int fd, int gno);
struct ext2_inode getinode(int ino, int fd);
void inode_data(struct ext2_inode inode, int fd, int choice, int ino);
void single(int fd, int block_size, int address, int choice);
void doub(int fd, int block_size, int address, int choice);
void triple(int fd, int block_size, int address, int choice);
void print_bitmap(unsigned char *block_bits, int num_bytes);
void group_count(int fd);

void directory(int fd);
#define SIZE 10000
int items[SIZE];
int front = -1, rear = -1;
int isFull();
int isEmpty();
void enQueue(int element);
int deQueue();
void display();

int main(int argc, char *argv[]){
    int fd;
    int count;
    int ino;
    int bgno, iindex, inode_size, block_size;
    unsigned long inode_offset;
    struct ext2_super_block sb;
    struct ext2_inode inode;
    //argv[3] is the funtion you want to perform
    int fno = atoi(argv[3]);
    //argv[2] is the no of group
    int gno = atoi(argv[2]);
    int choice = 1;
    fd = open(argv[1], O_RDONLY); //argv[1] = /dev/sda3
    if(fd == -1){
        perror("readsuper:");
        exit(errno);
    }
    lseek64(fd, 1024, SEEK_SET);
    count = read(fd, &sb, sizeof(struct ext2_super_block));
    inode_size = sb.s_inode_size;
    block_size = 1024 << sb.s_log_block_size;
    if(argc == 5)
        ino = atoi(argv[4]);
    else
        ino = 2;
    //reading the first block
    switch (fno)
    {
        case 0:
            superblock(fd);
            break;
        case 1:
            group_descriptor(fd);
            break;
        case 2:
            block_bitmap(fd,gno);
            break;
        case 3:
            inode_bitmap(fd,gno);
            break;
        case 4:
            inode_table(fd,gno);
            break;
        case 5:
            inode = getinode(ino/*54424*/,fd);
            inode_data(inode,fd,choice, ino);
            break;
        case 6:
            directory(fd);
            break;
        case 7:
            inode = getinode(ino,fd);
            inode_data(inode,fd,0,ino);
            break;
        case 8:
            group_count(fd);
            break;
        default:
            break;
    }
    return 0;
}


void superblock(int fd){
    int count;
    int bgno, iindex, inode_size, block_size;
    unsigned long inode_offset;
    struct ext2_super_block sb;
    sb = sblite(fd);
    block_size = 1024 << sb.s_log_block_size;
    printf("%d\n", sb.s_inodes_count);
    printf("%d\n", sb.s_blocks_count);
    printf("%d\n", sb.s_clusters_per_group);
    printf("%d\n", sb.s_free_blocks_count);
    printf("%d\n", sb.s_free_inodes_count);
    printf("%d\n", sb.s_first_data_block);
    printf("%d\n", block_size);
    printf("%d\n", sb.s_blocks_per_group);
    printf("%d\n", sb.s_inodes_per_group);
    printf("%d\n", sb.s_inode_size);
    printf("%d\n", sb.s_magic);
    inode_size = sb.s_inode_size;
}

struct ext2_super_block sblite(int fd){
    int count;
    struct ext2_super_block sb;
    lseek64(fd, 1024, SEEK_SET);
    count = read(fd, &sb, sizeof(struct ext2_super_block));
    return sb;
}

int block_off(int block_size){
    int block_offset;
    if((1024 + 1024)>block_size){
        block_offset = 1024 + block_size;
    }
    else{
        block_offset = block_size;
    }
    return block_offset;
}

int block(int block_size, int num){
    return BASE_OFFSET + (num - 1) * block_size;
}

void group_descriptor(int fd){
    int count, block_offset;
    int bgno, iindex, inode_size, block_size;
    struct ext2_group_desc bgdesc;
    struct ext2_super_block sb;
    sb = sblite(fd);
    block_size = 1024 << sb.s_log_block_size;
    block_offset = block_off(block_size);
    for(int i = 0; i < 500; i++){
        lseek64(fd,block_offset+i*sizeof(bgdesc),SEEK_SET);
        count = read(fd, &bgdesc, sizeof(struct ext2_group_desc));
        if(count == -1)
            return;
        if(bgdesc.bg_block_bitmap != 0)  
            printf("%d %d %d %d %d %d\n", bgdesc.bg_block_bitmap,bgdesc.bg_inode_bitmap,bgdesc.bg_inode_table,bgdesc.bg_free_blocks_count, bgdesc.bg_free_inodes_count, bgdesc.bg_used_dirs_count);
    }
}

void group_count(int fd){
    int count, block_offset;
    int bgno, iindex, inode_size, block_size;
    struct ext2_group_desc bgdesc;
    struct ext2_super_block sb;
    sb = sblite(fd);
    block_size = 1024 << sb.s_log_block_size;
    block_offset = block_off(block_size);
    int c = 0;
    for(int i = 0; i < 500; i++){
        lseek64(fd,block_offset+i*sizeof(bgdesc),SEEK_SET);
        count = read(fd, &bgdesc, sizeof(struct ext2_group_desc));
        if(bgdesc.bg_block_bitmap != 0)  
            c++;
    }
    printf("%i",c);
}

struct ext2_group_desc group_desc(int fd, int i){
    int count, block_offset;
    int bgno, iindex, inode_size, block_size;
    struct ext2_super_block sb;
    struct ext2_group_desc bgdesc;
    sb = sblite(fd);
    block_size = 1024 << sb.s_log_block_size;
    block_offset = block_off(block_size);
    lseek64(fd,block_offset+i*sizeof(bgdesc),SEEK_SET);
    count = read(fd, &bgdesc, sizeof(struct ext2_group_desc));
    return bgdesc;
}

void block_bitmap(int fd, int gno){
    unsigned char *bitmap;
    int block_size;
    int i, j, t;
    struct ext2_group_desc bgdesc;
    struct ext2_super_block sb;
    sb = sblite(fd);
    block_size = 1024 << sb.s_log_block_size;
    bgdesc = group_desc(fd,gno);
    bitmap = malloc(block_size);
    lseek64(fd,block(block_size,bgdesc.bg_block_bitmap),SEEK_SET);
    read(fd, bitmap, block_size);  
    int num_bytes = 10000;
    print_bitmap(bitmap, num_bytes);
}

void print_bitmap(unsigned char *block_bits, int num_bytes) {
    int byte;
    int bit;
    unsigned char in_use;
    int c = 0;
    for (byte = 0; byte < num_bytes; byte++) {
	    for (bit = 0; bit < 8; bit++) {
	        in_use = (block_bits[byte] & (1 << bit)) >> bit;
	        if(in_use == 1)
                c += 1;
	    }
        if(c == 8)
            printf("1");
        else
            printf("0");
        printf(" ");
        c = 0;
    }
    printf("\n");
    return;
}

void inode_bitmap(int fd, int gno){
    unsigned char *bitmap;
    int block_size;
    int i, j, t;
    int bits[8];
    struct ext2_group_desc bgdesc;
    struct ext2_super_block sb;
    sb = sblite(fd);
    block_size = 1024 << sb.s_log_block_size;
    bgdesc = group_desc(fd,gno);
    bitmap = malloc(block_size);
    lseek64(fd,block(block_size, bgdesc.bg_inode_bitmap),SEEK_SET);
    read(fd, bitmap, block_size);
    int num_bytes = 10000;
    print_bitmap(bitmap, num_bytes); 
}

void inode_table(int fd, int gno){
    int block_size, inode_offset, inode_size;
    struct ext2_group_desc bgdesc;
    struct ext2_super_block sb;
    struct ext2_inode inode;
    sb = sblite(fd);                        
    block_size = 1024 << sb.s_log_block_size;
    bgdesc = group_desc(fd,gno);
    inode_size = sb.s_inode_size;
    unsigned int inodes_per_block = block_size / sizeof(struct ext2_inode);
    unsigned int itable_blocks = sb.s_inodes_per_group / inodes_per_block;
    for(int i = 0; i < sb.s_inodes_per_group; i++){
        inode_offset = bgdesc.bg_inode_table * block_size + i * inode_size;
        int i_no = (gno) * sb.s_inodes_per_group + i + 1;
        inode = getinode(i_no,fd);
        int no_blocks = (int) (inode.i_blocks * 512) / block_size;
        if((int)no_blocks != 0 && (int)inode.i_size > 0){
            printf("%d %d %d %d %d %d %d\n",i_no,inode.i_uid,inode.i_size,inode.i_gid,inode.i_links_count,no_blocks,inode.i_flags);
        }
    } 
}

struct ext2_inode getinode(int ino, int fd){
    int count;
    int bgno, iindex, inode_size, block_size;
    unsigned long inode_offset;
    struct ext2_super_block sb;
    struct ext2_inode inode;
    struct ext2_group_desc bgdesc;
    
	lseek64(fd, 1024, SEEK_SET);
    count = read(fd, &sb, sizeof(struct ext2_super_block));
    inode_size = sb.s_inode_size;
    block_size = 1024 << sb.s_log_block_size;

    int block_offset;

    if((1024 + 1024)>block_size){
        block_offset = 1024 + block_size;
    }
    else{
        block_offset = block_size;
    }

    bgno = ceil((ino -1) / sb.s_inodes_per_group);
    iindex = (ino -1) % sb.s_inodes_per_group;
    lseek64(fd, block_offset + bgno * sizeof(bgdesc), SEEK_SET);
    count = read(fd, &bgdesc, sizeof(struct ext2_group_desc));
    inode_offset = bgdesc.bg_inode_table * block_size + iindex * inode_size;
    lseek64(fd, inode_offset, SEEK_SET);
    read(fd, &inode, sizeof(inode));
    return inode;
}

void inode_data(struct ext2_inode inode, int fd, int choice, int ino){
    int block_size;
    struct ext2_super_block sb;
    struct ext2_dir_entry_2 ext2_dirent;
    sb = sblite(fd);
    block_size = 1024 << sb.s_log_block_size;
    int no_blocks = (int) (inode.i_blocks * 512) / block_size;
    unsigned char c;
    int direc = 0;
    unsigned int cs = block_size / sizeof(char);
    unsigned int sz = block_size / sizeof(int);
    if(choice == 1)    
        printf("%d %d %d %d %u\n",ino,inode.i_size,inode.i_links_count,no_blocks,sz);        
    for(int i = 0; i < no_blocks; i++){
        if(i < EXT2_NDIR_BLOCKS){
            if(choice == 1)
                printf("%u\n", inode.i_block[i]);
            else{
                    lseek64(fd, block_size + (inode.i_block[i]-1)*block_size, SEEK_SET);
                    read(fd, &c, sizeof(c));
                    int k = 0; 
                    while (k < cs && c != EOF)
                    {
                        k++;
                        putchar(c);
                        read(fd, &c, sizeof(c));
                    }
            }
        }
        else if (i == EXT2_IND_BLOCK){   
            if(inode.i_block[i] != 0){                      /* single indirect block */
                printf("%u\n", inode.i_block[i]);
                single(fd,block_size,inode.i_block[i], choice);
            }
        }
        else if (i == EXT2_DIND_BLOCK){           
            if(inode.i_block[i] != 0){                 /* double indirect block */
                printf("%u\n", inode.i_block[i]);
                doub(fd,block_size,inode.i_block[i], choice);
            }
        }
        else if (i == EXT2_TIND_BLOCK){   
            if(inode.i_block[i] != 0){                     /* triple indirect block */
                printf("%u\n", inode.i_block[i]);
                triple(fd,block_size,inode.i_block[i], choice);
            }
        }
    }
}

void single(int fd, int block_size, int address, int choice){
    lseek64(fd, block_size + (address-1)*block_size, SEEK_SET);
    unsigned int sz = block_size / sizeof(int);
    unsigned int inode2[sz];
    read(fd, &inode2, sizeof(inode2));
    unsigned char c;
    unsigned int cs = block_size / sizeof(char);
    for(int j = 0; j < sz; j++){
        if(inode2[j] == 0){
            ;
        }
        else{
            if(choice == 1){
                printf("%u\n", inode2[j]);
            }
            else{
                lseek64(fd, block_size + (inode2[j]-1)*block_size, SEEK_SET);
                read(fd, &c, sizeof(c));
                int i = 0;
                while (c != EOF && i < cs)
                {
                    i++;
                    putchar(c);
                    read(fd, &c, sizeof(c));
                }
            }
        }
    }
}

//Funtion to print the block numbers pointed by double indirect block
void doub(int fd, int block_size, int address, int choice){
    lseek64(fd, block_size + (address-1)*block_size, SEEK_SET);
    unsigned int sz = block_size / sizeof(int);
    unsigned int inode2[sz];
    read(fd, &inode2, sizeof(inode2));
    for(int j = 0; j < sz; j++){
        if(inode2[j] != 0){
            printf("%u\n", inode2[j]);
            single(fd, block_size,inode2[j],choice);
        }
    }
}

//Funtion to print the block numbers pointed by triple indirect block
void triple(int fd, int block_size, int address, int choice){
    lseek64(fd, block_size + (address-1)*block_size, SEEK_SET);
    unsigned int sz = block_size / sizeof(int);
    unsigned int inode2[sz];
    read(fd, &inode2, sizeof(inode2));
    for(int j = 0; j < sz; j++){
        if(inode2[j] != 0){
            printf("%u\n", inode2[j]);
            doub(fd, block_size,inode2[j],choice);
        }
    }
}

void directory(int fd){
    int block_size;
    struct ext2_super_block sb;
    struct ext2_dir_entry_2 ext2_dirent;
    sb = sblite(fd);
    block_size = 1024 << sb.s_log_block_size;
    struct ext2_inode inode;
    enQueue(2);
    int i = 0;
    while(isEmpty() != 1){
        int ino = deQueue();
        inode = getinode(ino,fd);
        printf("%i\n",ino);
        int no_blocks = (int) (inode.i_blocks * 512) / block_size;
        for(int j = 0; j < no_blocks; j++){
            lseek64(fd, inode.i_block[j] * block_size, SEEK_SET);
            unsigned int size = 0;
            int total = inode.i_size;
            if(inode.i_size > block_size){
                total = block_size;
                if(j == no_blocks - 1)
                    total = inode.i_size - block_size*(j); 
            }
            while (size < total)
            {
                read(fd, &ext2_dirent, sizeof(ext2_dirent));             
                if(ext2_dirent.inode != 0){ 
                    char file_name[EXT2_NAME_LEN+1];
                    memcpy(file_name, ext2_dirent.name, ext2_dirent.name_len);
                    file_name[ext2_dirent.name_len] = '\0';
                    if(ext2_dirent.file_type == 2 && ext2_dirent.inode != 2 && ext2_dirent.inode != ino && strncmp(file_name,"..",2) != 0 && file_name[0] != '.'){
                        enQueue(ext2_dirent.inode);}
                    if(ext2_dirent.inode != 2 && ext2_dirent.inode != ino && strncmp(file_name,"..",2) != 0 && file_name[0] != '.'){
                        printf("%s %d %u\n", file_name, ext2_dirent.inode, ext2_dirent.file_type);}
                }
                lseek64(fd, ext2_dirent.rec_len - sizeof(ext2_dirent), SEEK_CUR);
                size += ext2_dirent.rec_len;
            }
        }
        i++;
    }
}

// Check if the queue is full
int isFull() {
  if ((front == rear + 1) || (front == 0 && rear == SIZE - 1)) return 1;
  return 0;
}

// Check if the queue is empty
int isEmpty() {
  if (front == -1) return 1;
  return 0;
}

// Adding an element
void enQueue(int element) {
  if (isFull())
    //printf("\n Queue is full!! \n");
    ;
  else {
    if (front == -1) front = 0;
    rear = (rear + 1) % SIZE;
    items[rear] = element;
    }
}

// Removing an element
int deQueue() {
  int element;
  if (isEmpty()) {
    return (-1);
  } else {
    element = items[front];
    if (front == rear) {
      front = -1;
      rear = -1;
    } 
    else {
      front = (front + 1) % SIZE;
    }
    return (element);
  }
}

// Display the queue
void display() {
  int i;
  if (isEmpty())
    //printf(" \n Empty Queue\n");
    ;
  else {
    printf("\n Front -> %d ", front);
    printf("\n Items -> ");
    for (i = front; i != rear; i = (i + 1) % SIZE) {
      printf("%d ", items[i]);
    }
    printf("%d ", items[i]);
    printf("\n Rear -> %d \n", rear);
  }
}

